# `SBApplicationAppProtectionAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 9 instance variables, 14 properties, 28 instance methods, 6 class methods

## Instance variables

```
@"APApplication" _appProtectionApplication;
B _shouldShield;
B _shouldHide;
B _nextShieldViewCreationShouldRequestUnshielding;
@"NSString" _displayName;
@"NSHashTable" _observers;
@"BSCompoundAssertion" _visibilityAssertions;
@"NSTimer" _shouldHideDebounceTimer;
@"SBAppProtectionCoordinator" _owningCoordinator;
```

## Properties

```
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (TB,R,N,GisHidden) hidden;
@property (TB,N,V_shouldHide) shouldHide;
@property (T@"BSCompoundAssertion",R,N,V_visibilityAssertions) visibilityAssertions;
@property (T@"NSTimer",&,N,V_shouldHideDebounceTimer) shouldHideDebounceTimer;
@property (TB,N,V_shouldShield) shouldShield;
@property (T@"SBAppProtectionCoordinator",W,N,V_owningCoordinator) owningCoordinator;
@property (T@"APApplication",R,N) appProtectionApplication;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TB,N,V_nextShieldViewCreationShouldRequestUnshielding) nextShieldViewCreationShouldRequestUnshielding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBApplicationAppProtectionAssistant _assistantForBundleIdentifier:applicationController:];
+[SBApplicationAppProtectionAssistant areAnyApplicationsHidden];
+[SBApplicationAppProtectionAssistant areAnyApplicationsLocked];
+[SBApplicationAppProtectionAssistant assistantForApplication:applicationController:];
+[SBApplicationAppProtectionAssistant shouldHideApplicationWithBundleIdentifier:applicationController:];
+[SBApplicationAppProtectionAssistant shouldShieldApplicationWithBundleIdentifier:applicationController:];
```

## Instance methods

```
-[SBApplicationAppProtectionAssistant initWithApplication:];
-[SBApplicationAppProtectionAssistant setOwningCoordinator:];
-[SBApplicationAppProtectionAssistant acquireVisibilityAssertionForReason:];
-[SBApplicationAppProtectionAssistant succinctDescriptionBuilder];
-[SBApplicationAppProtectionAssistant removeObserver:];
-[SBApplicationAppProtectionAssistant displayName];
-[SBApplicationAppProtectionAssistant _updateShouldHide];
-[SBApplicationAppProtectionAssistant requestUnshielding];
-[SBApplicationAppProtectionAssistant descriptionWithMultilinePrefix:];
-[SBApplicationAppProtectionAssistant owningCoordinator];
-[SBApplicationAppProtectionAssistant setShouldShield:];
-[SBApplicationAppProtectionAssistant succinctDescription];
-[SBApplicationAppProtectionAssistant addObserver:];
-[SBApplicationAppProtectionAssistant invalidate];
-[SBApplicationAppProtectionAssistant visibilityAssertions];
-[SBApplicationAppProtectionAssistant shouldHide];
-[SBApplicationAppProtectionAssistant isHidden];
-[SBApplicationAppProtectionAssistant setShouldHideDebounceTimer:];
-[SBApplicationAppProtectionAssistant appProtectionApplication];
-[SBApplicationAppProtectionAssistant shouldHideDebounceTimer];
-[SBApplicationAppProtectionAssistant setShouldHide:];
-[SBApplicationAppProtectionAssistant setNextShieldViewCreationShouldRequestUnshielding:];
-[SBApplicationAppProtectionAssistant nextShieldViewCreationShouldRequestUnshielding];
-[SBApplicationAppProtectionAssistant description];
-[SBApplicationAppProtectionAssistant shouldShield];
-[SBApplicationAppProtectionAssistant observers];
-[SBApplicationAppProtectionAssistant createShieldUIViewController];
-[SBApplicationAppProtectionAssistant descriptionBuilderWithMultilinePrefix:];
```
