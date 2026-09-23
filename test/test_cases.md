# Test Cases – Cybersecurity Asset Inventory

## TC01 – Add Asset
**Input:** Add a new asset with a unique Asset ID and valid values.  
**Expected:** `Asset added successfully!`

## TC02 – Display Assets
**Input:** Select option 2.  
**Expected:** All assets in `data/assets.json` are displayed.

## TC03 – Search Existing Asset
**Input:** Search for `A101`.  
**Expected:** HR-PC-01 details are displayed.

## TC04 – Search Non-existing Asset
**Input:** Search for `A999`.  
**Expected:** `Asset not found.`

## TC05 – Update Asset
**Input:** Update `A102` with valid information.  
**Expected:** `Asset updated successfully!`

## TC06 – Delete Asset
**Input:** Delete `A103`.  
**Expected:** `Asset deleted successfully!`

## TC07 – Invalid Asset Type
**Input:** Enter an asset type not in the allowed list.  
**Expected:** Program rejects the value and asks again.

## TC08 – Invalid Risk Level
**Input:** Enter an invalid risk level.  
**Expected:** Program rejects the value and asks again.

## TC09 – Invalid Security Status
**Input:** Enter an invalid status.  
**Expected:** Program rejects the value and asks again.

## TC10 – Security Summary
**Input:** Select option 6.  
**Expected:** Counts for total, risk levels, vulnerable, warning and secure assets are displayed.
