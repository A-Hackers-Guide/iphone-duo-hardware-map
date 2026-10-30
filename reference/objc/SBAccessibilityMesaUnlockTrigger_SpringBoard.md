# `SBAccessibilityMesaUnlockTrigger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMesaUnlockTrigger`
- Protocols: `SBMesaUnlockTriggerDelegate`
- 2 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBBiometricUnlockBehaviorConfigurationDelegate>" _behaviorConfigurationDelegate;
@"SBMesaUnlockTrigger" _baseTrigger;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAccessibilityMesaUnlockTrigger screenOff];
-[SBAccessibilityMesaUnlockTrigger bioUnlock];
-[SBAccessibilityMesaUnlockTrigger fingerOff];
-[SBAccessibilityMesaUnlockTrigger fingerOn];
-[SBAccessibilityMesaUnlockTrigger initWithUnlockBehaviorConfigurationDelegate:baseTrigger:];
-[SBAccessibilityMesaUnlockTrigger menuButtonDown];
-[SBAccessibilityMesaUnlockTrigger menuButtonUp];
-[SBAccessibilityMesaUnlockTrigger mesaUnlockTriggerFired:];
-[SBAccessibilityMesaUnlockTrigger significantUserInteractionOccurred];
```
