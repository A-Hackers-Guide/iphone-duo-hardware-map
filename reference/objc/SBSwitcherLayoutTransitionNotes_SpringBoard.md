# `SBSwitcherLayoutTransitionNotes`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 24 instance variables, 28 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _fromSwitcher;
B _fromApp;
B _fromHomeScreen;
B _fromManyApps;
B _inAnySwitcher;
B _inHomeScreen;
B _inApp;
B _inManyApps;
B _fromNoAppToApp;
B _fromHomeScreenToApp;
B _fromAppToHomeScreen;
B _stableInHomeScreen;
B _stableInAppOrMovingBetweenSingleApp;
B _stableInSameApp;
B _changingApps;
B _movingToSingleApp;
B _movingToManyApps;
B _movingFromManyApps;
B _isPIPRestore;
B _isSystemGesture;
B _isHomeButtonInitiated;
B _isRotation;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _inAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,W,N,V_fromAppLayout) fromAppLayout;
@property (TB,R,N,V_fromSwitcher) fromSwitcher;
@property (TB,R,N,V_fromApp) fromApp;
@property (TB,R,N,V_fromHomeScreen) fromHomeScreen;
@property (TB,R,N,V_fromManyApps) fromManyApps;
@property (T@"SBAppLayout",R,W,N,V_inAppLayout) inAppLayout;
@property (TB,R,N,V_inAnySwitcher) inAnySwitcher;
@property (TB,R,N,V_inHomeScreen) inHomeScreen;
@property (TB,R,N,V_inApp) inApp;
@property (TB,R,N,V_inManyApps) inManyApps;
@property (TB,R,N,V_fromNoAppToApp) fromNoAppToApp;
@property (TB,R,N,V_fromHomeScreenToApp) fromHomeScreenToApp;
@property (TB,R,N,V_fromAppToHomeScreen) fromAppToHomeScreen;
@property (TB,R,N,V_stableInHomeScreen) stableInHomeScreen;
@property (TB,R,N,V_stableInAppOrMovingBetweenSingleApp) stableInAppOrMovingBetweenSingleApp;
@property (TB,R,N,V_stableInSameApp) stableInSameApp;
@property (TB,R,N,V_changingApps) changingApps;
@property (TB,R,N,V_movingToSingleApp) movingToSingleApp;
@property (TB,R,N,V_movingToManyApps) movingToManyApps;
@property (TB,R,N,V_movingFromManyApps) movingFromManyApps;
@property (TB,R,N,V_isPIPRestore) isPIPRestore;
@property (TB,R,N,V_isSystemGesture) isSystemGesture;
@property (TB,R,N,V_isHomeButtonInitiated) isHomeButtonInitiated;
@property (TB,R,N,V_isRotation) isRotation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherLayoutTransitionNotes isPIPRestore];
-[SBSwitcherLayoutTransitionNotes inAppLayout];
-[SBSwitcherLayoutTransitionNotes movingToSingleApp];
-[SBSwitcherLayoutTransitionNotes fromNoAppToApp];
-[SBSwitcherLayoutTransitionNotes succinctDescriptionBuilder];
-[SBSwitcherLayoutTransitionNotes fromSwitcher];
-[SBSwitcherLayoutTransitionNotes initWithFromPreviousState:currentLayoutState:transitionRequest:];
-[SBSwitcherLayoutTransitionNotes inManyApps];
-[SBSwitcherLayoutTransitionNotes fromManyApps];
-[SBSwitcherLayoutTransitionNotes inAnySwitcher];
-[SBSwitcherLayoutTransitionNotes isRotation];
-[SBSwitcherLayoutTransitionNotes descriptionWithMultilinePrefix:];
-[SBSwitcherLayoutTransitionNotes fromAppLayout];
-[SBSwitcherLayoutTransitionNotes isHomeButtonInitiated];
-[SBSwitcherLayoutTransitionNotes succinctDescription];
-[SBSwitcherLayoutTransitionNotes stableInAppOrMovingBetweenSingleApp];
-[SBSwitcherLayoutTransitionNotes stableInSameApp];
-[SBSwitcherLayoutTransitionNotes fromApp];
-[SBSwitcherLayoutTransitionNotes movingToManyApps];
-[SBSwitcherLayoutTransitionNotes changingApps];
-[SBSwitcherLayoutTransitionNotes fromHomeScreenToApp];
-[SBSwitcherLayoutTransitionNotes fromHomeScreen];
-[SBSwitcherLayoutTransitionNotes description];
-[SBSwitcherLayoutTransitionNotes stableInHomeScreen];
-[SBSwitcherLayoutTransitionNotes inHomeScreen];
-[SBSwitcherLayoutTransitionNotes movingFromManyApps];
-[SBSwitcherLayoutTransitionNotes inApp];
-[SBSwitcherLayoutTransitionNotes fromAppToHomeScreen];
-[SBSwitcherLayoutTransitionNotes isSystemGesture];
-[SBSwitcherLayoutTransitionNotes descriptionBuilderWithMultilinePrefix:];
```
