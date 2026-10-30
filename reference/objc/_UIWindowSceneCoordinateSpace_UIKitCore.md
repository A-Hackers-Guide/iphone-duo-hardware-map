# `_UIWindowSceneCoordinateSpace`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UICoordinateSpace`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"FBSSceneSettings" _effectiveSettings;
@"UIWindowScene" _windowScene;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T@"UIWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIWindowSceneCoordinateSpace convertPoint:fromCoordinateSpace:];
-[_UIWindowSceneCoordinateSpace convertRect:toCoordinateSpace:];
-[_UIWindowSceneCoordinateSpace convertPoint:toCoordinateSpace:];
-[_UIWindowSceneCoordinateSpace convertRect:fromCoordinateSpace:];
-[_UIWindowSceneCoordinateSpace initWithWindowScene:effectiveSettings:];
-[_UIWindowSceneCoordinateSpace bounds];
-[_UIWindowSceneCoordinateSpace windowScene];
```
