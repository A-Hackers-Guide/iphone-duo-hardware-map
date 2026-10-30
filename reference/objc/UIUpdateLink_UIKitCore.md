# `UIUpdateLink`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 6 class methods

## Instance variables

```
{ActionListHead="slh_first"^{ActionListItem}} _actions;
{_UIUpdateRequest="flags"I"minRate"I"preferredRate"I"maxRate"I"phase"Q"load"Q} _request;
B _engaged;
B _active;
B _enabled;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N) requiresContinuousUpdates;
@property (TB,N) wantsLowLatencyEventDispatch;
@property (TB,N) wantsImmediatePresentation;
@property (T{CAFrameRateRange=fff},N) preferredFrameRateRange;
```

## Class methods

```
+[UIUpdateLink updateLinkForWindowScene:];
+[UIUpdateLink updateLinkForWindowScene:actionHandler:];
+[UIUpdateLink updateLinkForWindowScene:actionTarget:selector:];
+[UIUpdateLink updateLinkForView:];
+[UIUpdateLink updateLinkForView:actionHandler:];
+[UIUpdateLink updateLinkForView:actionTarget:selector:];
```

## Instance methods

```
-[UIUpdateLink setPreferredFrameRateRange:];
-[UIUpdateLink dealloc];
-[UIUpdateLink preferredFrameRateRange];
-[UIUpdateLink isEnabled];
-[UIUpdateLink setEnabled:];
-[UIUpdateLink addActionToPhase:handler:];
-[UIUpdateLink addActionToPhase:target:selector:];
-[UIUpdateLink addActionWithHandler:];
-[UIUpdateLink addActionWithTarget:selector:];
-[UIUpdateLink currentUpdateInfo];
-[UIUpdateLink requiresContinuousUpdates];
-[UIUpdateLink setRequiresContinuousUpdates:];
-[UIUpdateLink setWantsImmediatePresentation:];
-[UIUpdateLink setWantsLowLatencyEventDispatch:];
-[UIUpdateLink wantsImmediatePresentation];
-[UIUpdateLink wantsLowLatencyEventDispatch];
```
