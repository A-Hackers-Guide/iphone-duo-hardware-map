# `UIFocusUpdateContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 27 properties, 51 instance methods, 1 class methods

## Instance variables

```
{?="isValid"b1"hasValidated"b1"shouldUpdateDestinationItem"b1"sourceItemMayRemainFocused"b1"didResolveCommonAncestorEnvironment"b1} _flags;
B _deferredUpdate;
B _focusRedirectedByGuide;
@"_UIFocusGuideImpl" _focusedGuideImpl;
@"_UIFocusItemInfo" _destinationItemInfo;
@"<UIFocusEnvironment>" _commonAncestorEnvironment;
@"NSString" _previouslyFocusedGroupIdentifier;
@"NSString" _nextFocusedGroupIdentifier;
@"_UIDynamicFocusGroupMap" _focusGroupMap;
@"<_UIFocusBehavior>" _focusBehavior;
@"_UIFocusItemInfo" _sourceItemInfo;
@"_UIFocusMapSearchInfo" _focusMapSearchInfo;
@"<UIFocusEnvironment>" _initialDestinationEnvironment;
@"_UIDebugLogReport" _preferredFocusReport;
@"_UIDebugIssueReport" _validationReport;
@"<_UIFocusUpdateRequesting>" _request;
@"_UIFocusEnvironmentScrollableContainerTuple" _commonEnvironmentScrollableContainer;
@"_UIFocusMovementInfo" _focusMovement;
```

## Properties

```
@property (T@"UIView",R,W,N) previouslyFocusedView;
@property (T@"UIView",R,W,N) nextFocusedView;
@property (T@"_UIDynamicFocusGroupMap",&,N,G_focusGroupMap,S_setFocusGroupMap:,V_focusGroupMap) focusGroupMap;
@property (T@"<_UIFocusBehavior>",R,N,V_focusBehavior) focusBehavior;
@property (T@"_UIFocusItemInfo",R,C,N,G_sourceItemInfo,V_sourceItemInfo) sourceItemInfo;
@property (T@"_UIFocusItemInfo",R,C,N,G_destinationItemInfo,V_destinationItemInfo) destinationItemInfo;
@property (T@"_UIFocusMapSearchInfo",&,N,G_focusMapSearchInfo,S_setFocusMapSearchInfo:,V_focusMapSearchInfo) focusMapSearchInfo;
@property (T@"<UIFocusEnvironment>",R,W,N,G_initialDestinationEnvironment,V_initialDestinationEnvironment) initialDestinationEnvironment;
@property (T@"<UIFocusEnvironment>",R,W,N,G_commonAncestorEnvironment,V_commonAncestorEnvironment) commonAncestorEnvironment;
@property (TB,N,G_isDeferredUpdate,S_setDeferredUpdate:,V_deferredUpdate) deferredUpdate;
@property (T@"_UIFocusGuideImpl",W,N,S_setFocusedGuideImpl:,V_focusedGuideImpl) _focusedGuideImpl;
@property (T@"NSString",R,N,G_previouslyFocusedGroupIdentifier,V_previouslyFocusedGroupIdentifier) previouslyFocusedGroupIdentifier;
@property (T@"NSString",R,N,G_nextFocusedGroupIdentifier,V_nextFocusedGroupIdentifier) nextFocusedGroupIdentifier;
@property (Tq,R,N,G_groupFilter) groupFilter;
@property (T@"_UIDebugLogReport",&,N,G_preferredFocusReport,S_setPreferredFocusReport:,V_preferredFocusReport) preferredFocusReport;
@property (T@"_UIDebugIssueReport",&,N,G_validationReport,S_setValidationReport:,V_validationReport) validationReport;
@property (T@"<_UIFocusUpdateRequesting>",R,N,G_request,V_request) request;
@property (T@"_UIFocusEnvironmentScrollableContainerTuple",&,N,G_commonEnvironmentScrollableContainer,S_setCommonEnvironmentScrollableContainer:,V_commonEnvironmentScrollableContainer) commonEnvironmentScrollableContainer;
@property (T@"UIFocusGuide",R,W,N,G_focusedGuide) focusedGuide;
@property (TB,R,N,G_focusRedirectedByGuide,V_focusRedirectedByGuide) focusRedirectedByGuide;
@property (T{CGVector=dd},R,N,G_focusVelocity) focusVelocity;
@property (TB,R,N,G_isInitialMovement) isInitialMovement;
@property (T@"_UIFocusMovementInfo",R,N,G_focusMovement,V_focusMovement) focusMovement;
@property (T@"NSArray",R,N) linearSortedFocusItems;
@property (T@"<UIFocusItem>",R,W,N) previouslyFocusedItem;
@property (T@"<UIFocusItem>",R,W,N) nextFocusedItem;
@property (TQ,R,N) focusHeading;
```

## Class methods

```
+[UIFocusUpdateContext _defaultValidationReportFormatter];
```

## Instance methods

```
-[UIFocusUpdateContext init];
-[UIFocusUpdateContext _validate];
-[UIFocusUpdateContext focusHeading];
-[UIFocusUpdateContext description];
-[UIFocusUpdateContext _didUpdateFocus];
-[UIFocusUpdateContext nextFocusedView];
-[UIFocusUpdateContext _sourceItemInfo];
-[UIFocusUpdateContext nextFocusedItem];
-[UIFocusUpdateContext _cacheFocusBehavior];
-[UIFocusUpdateContext _commonAncestorEnvironment];
-[UIFocusUpdateContext _commonEnvironmentScrollableContainer];
-[UIFocusUpdateContext _destinationItemInfo];
-[UIFocusUpdateContext _focusGroupMap];
-[UIFocusUpdateContext _focusMapSearchInfo];
-[UIFocusUpdateContext _focusMovement];
-[UIFocusUpdateContext _focusRedirectedByGuide];
-[UIFocusUpdateContext _focusVelocity];
-[UIFocusUpdateContext _focusedGuide];
-[UIFocusUpdateContext _focusedGuideImpl];
-[UIFocusUpdateContext _groupFilter];
-[UIFocusUpdateContext _initWithContext:];
-[UIFocusUpdateContext _initWithFocusMovementRequest:nextFocusedItem:];
-[UIFocusUpdateContext _initWithFocusUpdateRequest:];
-[UIFocusUpdateContext _initialDestinationEnvironment];
-[UIFocusUpdateContext _isDeferredUpdate];
-[UIFocusUpdateContext _isFilteredToGroup];
-[UIFocusUpdateContext _isInitialMovement];
-[UIFocusUpdateContext _isValidInFocusSystem:];
-[UIFocusUpdateContext _nextFocusedGroupIdentifier];
-[UIFocusUpdateContext _preferredFocusReport];
-[UIFocusUpdateContext _previouslyFocusedGroupIdentifier];
-[UIFocusUpdateContext _request];
-[UIFocusUpdateContext _restoreRestrictedFocusMovementWithMovement:];
-[UIFocusUpdateContext _setCommonEnvironmentScrollableContainer:];
-[UIFocusUpdateContext _setDeferredUpdate:];
-[UIFocusUpdateContext _setFocusGroupMap:];
-[UIFocusUpdateContext _setFocusMapSearchInfo:];
-[UIFocusUpdateContext _setFocusRedirectedByGuide:];
-[UIFocusUpdateContext _setFocusedGuideImpl:];
-[UIFocusUpdateContext _setInitialDestinationEnvironment:];
-[UIFocusUpdateContext _setPreferredFocusReport:];
-[UIFocusUpdateContext _setSourceItemInfo:];
-[UIFocusUpdateContext _setValidationReport:];
-[UIFocusUpdateContext _updateDestinationItemIfNeeded];
-[UIFocusUpdateContext _updateWithFocusGroupMap:];
-[UIFocusUpdateContext _validationReport];
-[UIFocusUpdateContext _willUpdateFocusFromFocusedItem:];
-[UIFocusUpdateContext focusBehavior];
-[UIFocusUpdateContext linearSortedFocusItems];
-[UIFocusUpdateContext previouslyFocusedItem];
-[UIFocusUpdateContext previouslyFocusedView];
```
