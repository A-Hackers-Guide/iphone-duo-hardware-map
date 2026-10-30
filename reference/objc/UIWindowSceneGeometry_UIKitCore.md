# `UIWindowSceneGeometry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 6 instance variables, 12 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _interfaceOrientationLocked;
B _interactivelyResizing;
@"<UICoordinateSpace>" _coordinateSpace;
q _interfaceOrientation;
q _resizingRestrictions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _systemFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) systemFrame;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
@property (Tq,R,N) interfaceOrientation;
@property (TB,R,N,GisInterfaceOrientationLocked) interfaceOrientationLocked;
@property (T{CGSize=dd},R,D,N) minimumSize;
@property (T{CGSize=dd},R,D,N) maximumSize;
@property (Tq,R,N,V_resizingRestrictions) resizingRestrictions;
@property (TB,R,N,GisInteractivelyResizing) interactivelyResizing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWindowSceneGeometry isInterfaceOrientationLocked];
-[UIWindowSceneGeometry interfaceOrientation];
-[UIWindowSceneGeometry coordinateSpace];
-[UIWindowSceneGeometry debugDescription];
-[UIWindowSceneGeometry isInteractivelyResizing];
-[UIWindowSceneGeometry systemFrame];
-[UIWindowSceneGeometry description];
-[UIWindowSceneGeometry appendDescriptionToStream:];
-[UIWindowSceneGeometry resizingRestrictions];
-[UIWindowSceneGeometry copyWithZone:];
-[UIWindowSceneGeometry isEqual:];
```
