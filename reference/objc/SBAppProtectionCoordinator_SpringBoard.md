# `SBAppProtectionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `APSubjectMonitor`, `SBApplicationAppProtectionAssistantObserver`
- 3 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"BSCompoundAssertion" _suppressHidingAssertions;
@"APSystemAppOutlet" _systemAppOutlet;
@"NSMutableDictionary" _bundleIdentifiersToAssistants;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_bundleIdentifiersToAssistants) bundleIdentifiersToAssistants;
@property (T@"APSystemAppOutlet",&,N,V_systemAppOutlet) systemAppOutlet;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAppProtectionCoordinator isEnabled];
```

## Instance methods

```
-[SBAppProtectionCoordinator init];
-[SBAppProtectionCoordinator appProtectionSubjectsChanged:forSubscription:];
-[SBAppProtectionCoordinator dealloc];
-[SBAppProtectionCoordinator _updateShouldHide];
-[SBAppProtectionCoordinator systemAppOutlet];
-[SBAppProtectionCoordinator acquireSuppressHidingAppsAssertionForReason:];
-[SBAppProtectionCoordinator appProtectionAssistantShouldHideDidChange:];
-[SBAppProtectionCoordinator applicationsChanged:];
-[SBAppProtectionCoordinator assistantForApplication:];
-[SBAppProtectionCoordinator bundleIdentifiersToAssistants];
-[SBAppProtectionCoordinator noteAllScenesDismissedForAssistant:];
-[SBAppProtectionCoordinator noteSceneWillBecomeForegroundVisibleForAssistant:];
-[SBAppProtectionCoordinator setSystemAppOutlet:];
-[SBAppProtectionCoordinator shouldSuppressHiding];
```
