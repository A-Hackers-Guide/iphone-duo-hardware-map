# `_UITextEffectsWindowHostManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualStyleProviding`
- 1 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UITextEffectsWindow" _owningWindow;
```

## Properties

```
@property (T@"UITextEffectsWindow",R,W,V_owningWindow) owningWindow;
@property (T@"<UICoordinateSpace>",R,W) coordinateSpace;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) usableBounds;
```

## Instance methods

```
-[_UITextEffectsWindowHostManager coordinateSpace];
-[_UITextEffectsWindowHostManager initForOwningWindow:];
-[_UITextEffectsWindowHostManager interfaceOrientationDidChange];
-[_UITextEffectsWindowHostManager isExternallyPlaced];
-[_UITextEffectsWindowHostManager owningWindow];
-[_UITextEffectsWindowHostManager placeOwningWindowRelativeToResponder:];
-[_UITextEffectsWindowHostManager sceneBoundsDidChange];
-[_UITextEffectsWindowHostManager usableBounds];
```
