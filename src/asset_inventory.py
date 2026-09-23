import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "assets.json"

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


def load_assets():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_assets(assets):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(assets, file, indent=2)


def find_asset(assets, asset_id):
    for asset in assets:
        if asset["assetID"].lower() == asset_id.lower():
            return asset
    return None


def get_choice(prompt, choices):
    while True:
        value = input(prompt).strip()
        if value in choices:
            return value
        print(f"Invalid input. Choose one of: {', '.join(choices)}")


def add_asset(assets):
    print("\n========== ADD ASSET ==========")
    asset_id = input("Asset ID: ").strip()

    if find_asset(assets, asset_id):
        print("Asset ID already exists.")
        return

    asset = {
        "assetID": asset_id,
        "assetName": input("Asset Name: ").strip(),
        "assetType": get_choice(
            "Asset Type (Workstation/Server/Router/Switch/Application): ",
            ASSET_TYPES
        ),
        "ipAddress": input("IP Address: ").strip(),
        "operatingSystem": input("Operating System: ").strip(),
        "department": input("Department: ").strip(),
        "riskLevel": get_choice(
            "Risk Level (Low/Medium/High/Critical): ",
            RISK_LEVELS
        ),
        "securityStatus": get_choice(
            "Security Status (Secure/Warning/Vulnerable): ",
            SECURITY_STATUSES
        )
    }

    assets.append(asset)
    save_assets(assets)
    print("Asset added successfully!")


def display_asset(asset):
    print(f"Asset ID : {asset['assetID']}")
    print(f"Asset Name : {asset['assetName']}")
    print(f"Asset Type : {asset['assetType']}")
    print(f"IP Address : {asset['ipAddress']}")
    print(f"OS : {asset['operatingSystem']}")
    print(f"Department : {asset['department']}")
    print(f"Risk Level : {asset['riskLevel']}")
    print(f"Status : {asset['securityStatus']}")


def display_assets(assets):
    if not assets:
        print("No assets found.")
        return

    print("\n=========================================")
    print("      CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    for asset in assets:
        print()
        display_asset(asset)
        print("-----------------------------------------")

    print(f"Total Assets : {len(assets)}")


def search_asset(assets):
    print("\n========== SEARCH ASSET ==========")
    asset_id = input("Enter Asset ID: ").strip()
    asset = find_asset(assets, asset_id)

    if asset:
        print("\nAsset found:")
        display_asset(asset)
    else:
        print("Asset not found.")


def update_asset(assets):
    print("\n========== UPDATE ASSET ==========")
    asset_id = input("Enter Asset ID to update: ").strip()
    asset = find_asset(assets, asset_id)

    if not asset:
        print("Asset not found.")
        return

    asset["assetName"] = input("Asset Name: ").strip()
    asset["assetType"] = get_choice(
        "Asset Type (Workstation/Server/Router/Switch/Application): ",
        ASSET_TYPES
    )
    asset["ipAddress"] = input("IP Address: ").strip()
    asset["operatingSystem"] = input("Operating System: ").strip()
    asset["department"] = input("Department: ").strip()
    asset["riskLevel"] = get_choice(
        "Risk Level (Low/Medium/High/Critical): ",
        RISK_LEVELS
    )
    asset["securityStatus"] = get_choice(
        "Security Status (Secure/Warning/Vulnerable): ",
        SECURITY_STATUSES
    )

    save_assets(assets)
    print("Asset updated successfully!")


def delete_asset(assets):
    print("\n========== DELETE ASSET ==========")
    asset_id = input("Enter Asset ID to delete: ").strip()
    asset = find_asset(assets, asset_id)

    if not asset:
        print("Asset not found.")
        return

    assets.remove(asset)
    save_assets(assets)
    print("Asset deleted successfully!")


def security_summary(assets):
    print("\n========== SECURITY SUMMARY ==========")
    print(f"Total Assets : {len(assets)}")

    for risk in RISK_LEVELS:
        count = sum(a["riskLevel"] == risk for a in assets)
        print(f"{risk} Risk Assets : {count}")

    vulnerable = sum(
        a["securityStatus"] == "Vulnerable" for a in assets
    )
    warning = sum(
        a["securityStatus"] == "Warning" for a in assets
    )
    secure = sum(
        a["securityStatus"] == "Secure" for a in assets
    )

    print(f"Vulnerable Assets : {vulnerable}")
    print(f"Warning Assets : {warning}")
    print(f"Secure Assets : {secure}")
    print("======================================")


def main():
    assets = load_assets()

    while True:
        print("\n=========================================")
        print("   CYBERSECURITY ASSET INVENTORY SYSTEM")
        print("=========================================")
        print("1. Add Asset")
        print("2. Display Assets")
        print("3. Search Asset")
        print("4. Update Asset")
        print("5. Delete Asset")
        print("6. Security Summary")
        print("7. Exit")
        print("-----------------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            security_summary(assets)
        elif choice == "7":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Enter 1 to 7.")


if __name__ == "__main__":
    main()
