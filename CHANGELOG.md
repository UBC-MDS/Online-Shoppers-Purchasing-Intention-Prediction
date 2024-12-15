## CHANGELOG

All notable changes to this project in response to feedback will be documented in this file.  
You can also view the issue for tracking all of the below changes [here](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/122).

**Addressed feedback from release 0.0.1**: The introduction in report should have a specific question you are trying to solve.  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/133>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/132>  
**Commit**: [0d1729a](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/134/commits/0d1729af573b305e32de7117298786a40a91b613)  
**File updated**: `reports/online_shoppers_purchasing_intention_prediction.qmd` (line 50)  
**Implemented by**: Julian Daduica.

**Addressed feedback from release 0.0.1**: The discussion in report should reflect on the impact of your findings in real practice, infer what PageValue means, or how it's calculated, or why a low ExitRate is desirable.  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/130>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/131>  
**Commit**: [50add9f](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/131/commits/50add9fc90cf27eae1fbe868ddbe8f3ca2a7e86f)  
**File updated**: `reports/online_shoppers_purchasing_intention_prediction.qmd` (lines 120-125)  
**Implemented by**: Julian Daduica.

**Addressed feedback from Hankun's peer review**: In the script 04_preprocess_and_validate.py, from lines 40–55, a single variable could be used to save the columns to be dropped in a list. This would improve consistency and make it easier to update the columns in the future.  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/143>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/142>  
**Commit**: [ed2d1bb](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/142/commits/ed2d1bb313137d77484353747d486c475ccccbcb)  
**File updated**: `scripts/04_preprocess_and_validate.py` (line 44)  
**Implemented by**: Stephanie Ta.

**Addressed feedback from release 0.0.1**: Add a way under enforcement so the team can be contacted (e.g. an email, a link to some sort of contact form, etc.).  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/145>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/146>  
**Commit**: [48e1af1](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/146/commits/48e1af1886eb4e0b64d58294199788d214b1a5a2)  
**File updated**: `CODE_OF_CONDUCT.md` (line 37)  
**Implemented by**: Stephanie Ta.

**Addressed feedback from release 0.0.1**: Incorporate referencing to figures and tables in your text (otherwise, what's the purpose of having them?).  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/147>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/104>  
**Commit**: [e163fb5](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/commit/e163fb52e0397b5fb38abe23c705d0967ff75bd7)  
**File updated**: `‎reports/online_shoppers_purchasing_intention_prediction.qmd` (lines 92, 94, 108, 120, and 132)  
**Implemented by**: Stephanie Ta.

**Addressed feedback from Hankun's peer review**: Data Section Format in the Final Report: On pages 2–3 of the final PDF report, in the data section, displaying feature descriptions in a table or bullet-point format would make it easier to read.  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/149>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/148>  
**Commit**: [f00c400](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/commit/f00c4003e7e044ae3690450336b62dcc79179cda)  
**File updated**: 
`online_shoppers_purchasing_intention_prediction.html`
`online_shoppers_purchasing_intention_prediction.pdf`
`online_shoppers_purchasing_intention_prediction.qmd`  
**Implemented by**: Wai Ming Wong

**Addressed feedback from Rubia**: We seem to be getting a lot of warning messages that can be ignored when the 06_tune_and_train.py is run. These messages flood the user's terminal and can be overwhelming. To address this, we should suppress warnings for this script.  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/150>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/151>  
**Commit**: [f88416e](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/151/commits/f88416eda4fcb8a2da2892af79a677dee06ccfff)  
**File updated**: `scripts/06_tune_and_train.py` (line 40)  
**Implemented by**: Wai Ming Wong

**Addressed feedback from release 0.0.1**: Programming language and/or package versions are pinned using >= instead of =. This means that each time the environment is built in the future, the most recent version of the programming language and/or package will be installed in the environment. This will lead to the environment not being able to be reproducibly built in the future.  
**Issue**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/issues/128>  
**Pull request**: <https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120>  
**Commit**: [77e0a44](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120/commits/77e0a4438d061f0f746fc23a464e9c649212292e)  
[a88b517](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120/commits/a88b517062affdcd5db5c99113f5d61f87c69e76)  
[49cb757](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120/commits/49cb757fcd0afeadac919bc9bbb851e5fc8f520f)  
[36ee676](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120/commits/36ee6762ec52ad5178455cacaac66ee3e68ecc11)  
[90198a0](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120/commits/90198a03aa902da4bcab0881fcb4e3efd4f6d29f)  
[79606d3](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/pull/120/commits/79606d3415dc78022968d59848374b197fa245bc)  
**File updated**: 
`Dockerfile`
`conda-linux-64.lock`
`docker-compose.yml`
`environment.yaml`  
**Implemented by**: Wai Ming Wong
