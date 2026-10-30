# `_UIFocusScrollRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _scrollOffsetResolver;
@"_UIFocusItemInfo" _focusItemInfo;
@"_UIFocusMovementInfo" _focusMovement;
@"_UIFocusEnvironmentScrollableContainerTuple" _environmentScrollableContainer;
{CGPoint="x"d"y"d} _originatingContentOffset;
{CGPoint="x"d"y"d} _targetContentOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _focusItemFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originatingBounds;
```

## Properties

```
@property (TQ,R,N,V_scrollOffsetResolver) scrollOffsetResolver;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_originatingBounds) originatingBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_focusItemFrame) focusItemFrame;
@property (T{CGPoint=dd},R,N,V_originatingContentOffset) originatingContentOffset;
@property (T{CGPoint=dd},R,N,V_targetContentOffset) targetContentOffset;
@property (T@"_UIFocusItemInfo",R,N,V_focusItemInfo) focusItemInfo;
@property (T@"_UIFocusMovementInfo",R,N,V_focusMovement) focusMovement;
@property (T@"_UIFocusEnvironmentScrollableContainerTuple",R,N,V_environmentScrollableContainer) environmentScrollableContainer;
```

## Instance methods

```
-[_UIFocusScrollRequest description];
-[_UIFocusScrollRequest targetContentOffset];
-[_UIFocusScrollRequest environmentScrollableContainer];
-[_UIFocusScrollRequest focusItemFrame];
-[_UIFocusScrollRequest focusItemInfo];
-[_UIFocusScrollRequest focusMovement];
-[_UIFocusScrollRequest initWithBaseRequest:environmentScrollableContainer:];
-[_UIFocusScrollRequest initWithEnvironmentScrollableContainer:focusItemFrame:targetContentOffsetValue:];
-[_UIFocusScrollRequest initWithEnvironmentScrollableContainer:focusItemInfo:focusMovement:focusItemFrame:targetContentOffsetValue:];
-[_UIFocusScrollRequest initWithEnvironmentScrollableContainer:focusItemInfo:focusUpdateContext:];
-[_UIFocusScrollRequest initWithEnvironmentScrollableContainer:focusItemInfo:targetContentOffsetValue:];
-[_UIFocusScrollRequest originatingBounds];
-[_UIFocusScrollRequest originatingContentOffset];
-[_UIFocusScrollRequest reloadFocusItemInfo];
-[_UIFocusScrollRequest resolveTargetContentOffsetUsingScrollOffsetResolverClamped:];
-[_UIFocusScrollRequest scrollOffsetResolver];
```
