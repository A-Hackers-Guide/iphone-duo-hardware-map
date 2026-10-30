# `SBMainDisplaySystemGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemGestureManager`
- Protocols: `SBFZStackParticipantDelegate`, `PTSettingsKeyObserver`
- 4 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayIdentity" _displayIdentity;
B _multitaskingGesturesEnabled;
@"SBFZStackParticipant" _accessibilityZStackParticipant;
@"SBSystemGesturesSettings" _systemGesturesSettings;
```

## Properties

```
@property (T@"SBFZStackParticipant",&,N,V_accessibilityZStackParticipant) accessibilityZStackParticipant;
@property (T@"SBSystemGesturesSettings",&,N,V_systemGesturesSettings) systemGesturesSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMainDisplaySystemGestureManager zStackParticipant:updatePreferences:];
-[SBMainDisplaySystemGestureManager initWithDisplayIdentity:];
-[SBMainDisplaySystemGestureManager dealloc];
-[SBMainDisplaySystemGestureManager zStackParticipantDidChange:];
-[SBMainDisplaySystemGestureManager settings:changedValueForKey:];
-[SBMainDisplaySystemGestureManager descriptionBuilderWithMultilinePrefix:];
-[SBMainDisplaySystemGestureManager _initWithDisplayIdentity:];
-[SBMainDisplaySystemGestureManager _isGestureWithTypeAllowed:];
-[SBMainDisplaySystemGestureManager _setSystemGesturesDisabled:];
-[SBMainDisplaySystemGestureManager _shouldEnableSystemGestureWithType:];
-[SBMainDisplaySystemGestureManager accessibilityZStackParticipant];
-[SBMainDisplaySystemGestureManager setAccessibilityZStackParticipant:];
-[SBMainDisplaySystemGestureManager setSystemGesturesDisabledForAccessibility:];
-[SBMainDisplaySystemGestureManager setSystemGesturesSettings:];
-[SBMainDisplaySystemGestureManager shouldSystemGestureReceiveTouchWithLocation:];
-[SBMainDisplaySystemGestureManager systemGesturesSettings];
```
