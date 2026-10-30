# `SBDataPlanFailureAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDataPlanAccountAlertItem`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSString" _carrierName;
B _newAccount;
```

## Properties

```
@property (T@"NSString",C,N,V_carrierName) carrierName;
@property (TB,N,GisNewAccount,V_newAccount) newAccount;
```

## Class methods

```
+[SBDataPlanFailureAlertItem laterButtonTitle];
+[SBDataPlanFailureAlertItem nowButtonTitle];
```

## Instance methods

```
-[SBDataPlanFailureAlertItem carrierName];
-[SBDataPlanFailureAlertItem setCarrierName:];
-[SBDataPlanFailureAlertItem configure:requirePasscodeForActions:];
-[SBDataPlanFailureAlertItem isNewAccount];
-[SBDataPlanFailureAlertItem initWithAccountURL:carrierName:newAccount:applicationController:];
-[SBDataPlanFailureAlertItem setNewAccount:];
```
