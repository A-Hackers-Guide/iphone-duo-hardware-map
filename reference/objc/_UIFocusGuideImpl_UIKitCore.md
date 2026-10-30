# `_UIFocusGuideImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusRegionContainer`, `_UIFocusGuideRegionDelegate`, `UIFocusItem`
- 6 instance variables, 29 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"<_UIFocusGuideImplDelegate>" _retainedDelegate;
Q _focusUpdateCount;
{?="isEnabled"b1"isUnoccludable"b1"isUnclippable"b1"focusPriorityRequired"b1"ignoresSpeedBumpEdges"b1"didSetPreferredFocusedEnvironments"b1"automaticallyPreferOwningItem"b1"delegatePreferredEnvironmentsForHeading"b1} _flags;
@"NSArray" _preferredFocusEnvironments;
@"<_UIFocusGuideImplDelegate>" _delegate;
@"<UIFocusItem>" _owningItem;
```

## Properties

```
@property (T@"<_UIFocusGuideImplDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,GisEnabled) enabled;
@property (T@"NSArray",C,N,V_preferredFocusEnvironments) preferredFocusEnvironments;
@property (TB,N,S_setDidSetPreferredFocusedEnvironments:) _didSetPreferredFocusedEnvironments;
@property (TB,N,S_setAutomaticallyPreferOwningItem:) _automaticallyPreferOwningItem;
@property (T@"<UIFocusItem>",W,N,V_owningItem) owningItem;
@property (TB,N,S_setIsUnoccludable:) _isUnoccludable;
@property (TB,N,S_setFocusPriorityRequired:) _focusPriorityRequired;
@property (TB,N,S_setIgnoresSpeedBumpEdges:) _ignoresSpeedBumpEdges;
@property (TB,N,S_setIsUnclippable:) _isUnclippable;
@property (TB,?,R,N,G_isEligibleForFocusInteraction) eligibleForFocusInteraction;
@property (TB,?,R,N,G_isEligibleForFocusOcclusion) eligibleForFocusOcclusion;
@property (Tq,?,R,N,G_preferredFocusMovementStyle) preferredFocusMovementStyle;
@property (T@"NSArray",?,R,C,N,G_linearFocusMovementSequences) linearFocusMovementSequences;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIFocusItem>",?,R,N) focusItemForSorting;
@property (TB,R,N) canBecomeFocused;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T@"UIFocusEffect",?,R,C,N) focusEffect;
@property (Tq,?,R,N) focusGroupPriority;
@property (Tq,?,R,N) focusItemDeferralMode;
@property (TB,?,R,N) isTransparentFocusItem;
```

## Instance methods

```
-[_UIFocusGuideImpl _isEligibleForFocusInteraction];
-[_UIFocusGuideImpl updateFocusIfNeeded];
-[_UIFocusGuideImpl _preferredFocusRegionCoordinateSpace];
-[_UIFocusGuideImpl initWithDelegate:];
-[_UIFocusGuideImpl init];
-[_UIFocusGuideImpl didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIFocusGuideImpl setNeedsFocusUpdate];
-[_UIFocusGuideImpl setPreferredFocusEnvironments:];
-[_UIFocusGuideImpl parentFocusEnvironment];
-[_UIFocusGuideImpl focusItemContainer];
-[_UIFocusGuideImpl canBecomeFocused];
-[_UIFocusGuideImpl isEnabled];
-[_UIFocusGuideImpl _uili_isFocusGuide];
-[_UIFocusGuideImpl setEnabled:];
-[_UIFocusGuideImpl delegate];
-[_UIFocusGuideImpl description];
-[_UIFocusGuideImpl preferredFocusEnvironments];
-[_UIFocusGuideImpl shouldUpdateFocusInContext:];
-[_UIFocusGuideImpl frame];
-[_UIFocusGuideImpl stopFocusUpdate];
-[_UIFocusGuideImpl _isUnoccludable];
-[_UIFocusGuideImpl _automaticallyPreferOwningItem];
-[_UIFocusGuideImpl _didSetPreferredFocusedEnvironments];
-[_UIFocusGuideImpl _focusPriorityRequired];
-[_UIFocusGuideImpl _ignoresSpeedBumpEdges];
-[_UIFocusGuideImpl _isUnclippable];
-[_UIFocusGuideImpl _searchForFocusRegionsInContext:];
-[_UIFocusGuideImpl _setAutomaticallyPreferOwningItem:];
-[_UIFocusGuideImpl _setDidSetPreferredFocusedEnvironments:];
-[_UIFocusGuideImpl _setFocusPriorityRequired:];
-[_UIFocusGuideImpl _setIgnoresSpeedBumpEdges:];
-[_UIFocusGuideImpl _setIsUnclippable:];
-[_UIFocusGuideImpl _setIsUnoccludable:];
-[_UIFocusGuideImpl focusDidUpdateViaGuide];
-[_UIFocusGuideImpl focusGuideRegion:preferredFocusEnvironmentsForMovementRequest:];
-[_UIFocusGuideImpl focusGuideRegion:willParticipateAsDestinationRegionInFocusUpdate:];
-[_UIFocusGuideImpl focusItemForSorting];
-[_UIFocusGuideImpl owningItem];
-[_UIFocusGuideImpl setOwningItem:];
-[_UIFocusGuideImpl startFocusUpdate];
```
