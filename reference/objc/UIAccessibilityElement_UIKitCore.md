# `UIAccessibilityElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UIFocusItem`, `UIFocusItemContainer`, `_UIFocusEnvironmentPrivate`, `UIAccessibilityIdentification`
- 1 instance variables, 29 properties, 32 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _accessibilityFrameInContainerSpace;
```

## Properties

```
@property (T@,W,D,N) accessibilityContainer;
@property (TB,N) isAccessibilityElement;
@property (T@"NSString",&,N) accessibilityLabel;
@property (T@"NSString",&,N) accessibilityHint;
@property (T@"NSString",&,N) accessibilityValue;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) accessibilityFrame;
@property (TQ,N) accessibilityTraits;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_accessibilityFrameInContainerSpace) accessibilityFrameInContainerSpace;
@property (TB,R,N) canBecomeFocused;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T@"UIFocusEffect",?,R,C,N) focusEffect;
@property (Tq,?,R,N) focusGroupPriority;
@property (Tq,?,R,N) focusItemDeferralMode;
@property (TB,?,R,N) isTransparentFocusItem;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
@property (TB,?,R,N,G_isEligibleForFocusInteraction) eligibleForFocusInteraction;
@property (TB,?,R,N,G_isEligibleForFocusOcclusion) eligibleForFocusOcclusion;
@property (Tq,?,R,N,G_preferredFocusMovementStyle) preferredFocusMovementStyle;
@property (T@"NSArray",?,R,C,N,G_linearFocusMovementSequences) linearFocusMovementSequences;
@property (T@"NSString",C,D,N) accessibilityIdentifier;
```

## Instance methods

```
-[UIAccessibilityElement _destroyFocusLayer];
-[UIAccessibilityElement _updateFocusLayerFrame];
-[UIAccessibilityElement updateFocusIfNeeded];
-[UIAccessibilityElement accessibilityFrame];
-[UIAccessibilityElement coordinateSpace];
-[UIAccessibilityElement focusItemsInRect:];
-[UIAccessibilityElement accessibilityTraits];
-[UIAccessibilityElement didUpdateFocusInContext:withAnimationCoordinator:];
-[UIAccessibilityElement setAccessibilityFrame:];
-[UIAccessibilityElement setNeedsFocusUpdate];
-[UIAccessibilityElement dealloc];
-[UIAccessibilityElement setAccessibilityTraits:];
-[UIAccessibilityElement accessibilityHint];
-[UIAccessibilityElement initWithAccessibilityContainer:];
-[UIAccessibilityElement parentFocusEnvironment];
-[UIAccessibilityElement focusItemContainer];
-[UIAccessibilityElement setIsAccessibilityElement:];
-[UIAccessibilityElement canBecomeFocused];
-[UIAccessibilityElement setAccessibilityValue:];
-[UIAccessibilityElement accessibilityLabel];
-[UIAccessibilityElement isAccessibilityElement];
-[UIAccessibilityElement preferredFocusEnvironments];
-[UIAccessibilityElement isTransparentFocusItem];
-[UIAccessibilityElement nextResponder];
-[UIAccessibilityElement setAccessibilityLabel:];
-[UIAccessibilityElement setAccessibilityHint:];
-[UIAccessibilityElement shouldUpdateFocusInContext:];
-[UIAccessibilityElement accessibilityValue];
-[UIAccessibilityElement frame];
-[UIAccessibilityElement _firstViewAncestor];
-[UIAccessibilityElement accessibilityFrameInContainerSpace];
-[UIAccessibilityElement setAccessibilityFrameInContainerSpace:];
```
