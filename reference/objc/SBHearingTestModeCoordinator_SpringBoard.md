# `SBHearingTestModeCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSUIHearingTestModeHostComponentDelegate`
- 6 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSHashTable" _observers;
B _isConfiguringSinks;
@"NSMutableSet" _identifiersForHearingTestModeActiveProviders;
@"SBSUIHearingTestModeHostComponent" _hearingTestModeHostComponent;
@"DNDModeSelectionService" _dndService;
q _hearingTestMode;
```

## Properties

```
@property (Tq,N,V_hearingTestMode) hearingTestMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBHearingTestModeCoordinator dndHearingTestModeClientIdentifier];
+[SBHearingTestModeCoordinator dndModeAssertionClientIdentifier];
```

## Instance methods

```
-[SBHearingTestModeCoordinator setHearingTestMode:];
-[SBHearingTestModeCoordinator removeObserver:];
-[SBHearingTestModeCoordinator init];
-[SBHearingTestModeCoordinator addObserver:];
-[SBHearingTestModeCoordinator hearingTestMode];
-[SBHearingTestModeCoordinator hearingTestModeHostComponentDidChangeActiveState:];
-[SBHearingTestModeCoordinator _acquireDNDModeAssertion];
-[SBHearingTestModeCoordinator _invalidateDNDModeAssertion];
-[SBHearingTestModeCoordinator _noteHearingTestModeActiveForProviderWithIdentifier:];
-[SBHearingTestModeCoordinator _noteHearingTestModeInactiveForProviderWithIdentifier:];
-[SBHearingTestModeCoordinator _recalculateHearingTestMode];
-[SBHearingTestModeCoordinator _setDNDHearingTestModeActive:];
-[SBHearingTestModeCoordinator addSceneExtensionIfNeeded:];
```
