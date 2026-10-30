# `SBDataPlanAccountAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDataPlanAlertItem`
- Protocols: `SBDataPlanAlertActions`
- 2 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSURL" _accountURL;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"NSURL",C,N,V_accountURL) accountURL;
```

## Class methods

```
+[SBDataPlanAccountAlertItem laterButtonTitle];
+[SBDataPlanAccountAlertItem nowButtonTitle];
```

## Instance methods

```
-[SBDataPlanAccountAlertItem configure:requirePasscodeForActions:];
-[SBDataPlanAccountAlertItem accountURL];
-[SBDataPlanAccountAlertItem notNow];
-[SBDataPlanAccountAlertItem initWithAccountURL:applicationController:];
-[SBDataPlanAccountAlertItem setAccountURL:];
-[SBDataPlanAccountAlertItem takeAction];
```
