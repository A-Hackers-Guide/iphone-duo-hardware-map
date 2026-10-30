# `SBAlwaysOnSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
q _sideButtonBehavior;
@"SBAlwaysOnPolicySettings" _policySettings;
@"SBAlwaysOnAPLSettings" _aplSettings;
```

## Properties

```
@property (Tq,N,V_sideButtonBehavior) sideButtonBehavior;
@property (T@"SBAlwaysOnPolicySettings",&,N,V_policySettings) policySettings;
@property (T@"SBAlwaysOnAPLSettings",&,N,V_aplSettings) aplSettings;
```

## Class methods

```
+[SBAlwaysOnSettings settingsControllerModule];
```

## Instance methods

```
-[SBAlwaysOnSettings setDefaultValues];
-[SBAlwaysOnSettings setAplSettings:];
-[SBAlwaysOnSettings aplSettings];
-[SBAlwaysOnSettings policySettings];
-[SBAlwaysOnSettings setPolicySettings:];
-[SBAlwaysOnSettings setSideButtonBehavior:];
-[SBAlwaysOnSettings sideButtonBehavior];
```
