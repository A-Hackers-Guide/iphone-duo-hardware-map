# `_UIFocusRegionSearchContextState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"<_UIFocusRegionContainer>" _regionContainer;
@"UIFocusSystem" _regionContainerFocusSystem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _clippingRect;
```

## Properties

```
@property (T@"<_UIFocusRegionContainer>",R,N,V_regionContainer) regionContainer;
@property (T@"UIFocusSystem",R,N,V_regionContainerFocusSystem) regionContainerFocusSystem;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_clippingRect) clippingRect;
```

## Class methods

```
+[_UIFocusRegionSearchContextState stateWithRegionContainer:focusSystem:clippingRect:];
```

## Instance methods

```
-[_UIFocusRegionSearchContextState regionContainer];
-[_UIFocusRegionSearchContextState clippingRect];
-[_UIFocusRegionSearchContextState initWithRegionContainer:focusSystem:clippingRect:];
-[_UIFocusRegionSearchContextState regionContainerFocusSystem];
```
