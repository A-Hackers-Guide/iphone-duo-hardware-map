# `UIEditMenuConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 23 instance methods, 1 class methods

## Instance variables

```
B __ignoresPassthroughInView;
B __prefersMenuPresentationInView;
B __ignoresKeyboardAvoidance;
B __didHandoff;
@"<NSCopying>" _identifier;
q _preferredArrowDirection;
@"UIResponder" __firstResponderTarget;
@"UIWindow" __overrideSourceWindow;
Q __preferredElementDisplayMode;
@"_UIMenuPresentationSource" __presentationSource;
{CGPoint="x"d"y"d} _sourcePoint;
```

## Properties

```
@property (T@"<NSCopying>",C,N,V_identifier) identifier;
@property (T{CGPoint=dd},N,V_sourcePoint) sourcePoint;
@property (TB,N,V__ignoresPassthroughInView) _ignoresPassthroughInView;
@property (TB,N,V__prefersMenuPresentationInView) _prefersMenuPresentationInView;
@property (T@"UIResponder",W,N,V__firstResponderTarget) _firstResponderTarget;
@property (T@"UIWindow",W,N,V__overrideSourceWindow) _overrideSourceWindow;
@property (TB,N,V__ignoresKeyboardAvoidance) _ignoresKeyboardAvoidance;
@property (TQ,N,V__preferredElementDisplayMode) _preferredElementDisplayMode;
@property (TB,N,S_setDidHandoff:,V__didHandoff) _didHandoff;
@property (T@"_UIMenuPresentationSource",&,N,V__presentationSource) _presentationSource;
@property (Tq,N,V_preferredArrowDirection) preferredArrowDirection;
```

## Class methods

```
+[UIEditMenuConfiguration configurationWithIdentifier:sourcePoint:];
```

## Instance methods

```
-[UIEditMenuConfiguration set_ignoresPassthroughInView:];
-[UIEditMenuConfiguration identifier];
-[UIEditMenuConfiguration _overrideSourceWindow];
-[UIEditMenuConfiguration _firstResponderTarget];
-[UIEditMenuConfiguration _prefersMenuPresentationInView];
-[UIEditMenuConfiguration preferredArrowDirection];
-[UIEditMenuConfiguration set_firstResponderTarget:];
-[UIEditMenuConfiguration _ignoresPassthroughInView];
-[UIEditMenuConfiguration set_ignoresKeyboardAvoidance:];
-[UIEditMenuConfiguration setIdentifier:];
-[UIEditMenuConfiguration _preferredElementDisplayMode];
-[UIEditMenuConfiguration _setDidHandoff:];
-[UIEditMenuConfiguration _didHandoff];
-[UIEditMenuConfiguration set_prefersMenuPresentationInView:];
-[UIEditMenuConfiguration set_preferredElementDisplayMode:];
-[UIEditMenuConfiguration setPreferredArrowDirection:];
-[UIEditMenuConfiguration description];
-[UIEditMenuConfiguration sourcePoint];
-[UIEditMenuConfiguration set_overrideSourceWindow:];
-[UIEditMenuConfiguration setSourcePoint:];
-[UIEditMenuConfiguration _ignoresKeyboardAvoidance];
-[UIEditMenuConfiguration set_presentationSource:];
-[UIEditMenuConfiguration _presentationSource];
```
