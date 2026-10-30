# `SBSceneLayoutCoordinateSpace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `UICoordinateSpace`
- 1 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"<UICoordinateSpace>" _parentCoordinateSpace;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
```

## Class methods

```
+[SBSceneLayoutCoordinateSpace coordinateSpaceForFrame:withinCoordinateSpace:];
+[SBSceneLayoutCoordinateSpace coordinateSpaceForInterfaceOrientation:withReferenceCoordinateSpace:inOrientation:];
```

## Instance methods

```
-[SBSceneLayoutCoordinateSpace succinctDescriptionBuilder];
-[SBSceneLayoutCoordinateSpace convertPoint:fromCoordinateSpace:];
-[SBSceneLayoutCoordinateSpace convertRect:toCoordinateSpace:];
-[SBSceneLayoutCoordinateSpace descriptionWithMultilinePrefix:];
-[SBSceneLayoutCoordinateSpace convertPoint:toCoordinateSpace:];
-[SBSceneLayoutCoordinateSpace succinctDescription];
-[SBSceneLayoutCoordinateSpace convertRect:fromCoordinateSpace:];
-[SBSceneLayoutCoordinateSpace bounds];
-[SBSceneLayoutCoordinateSpace description];
-[SBSceneLayoutCoordinateSpace descriptionBuilderWithMultilinePrefix:];
-[SBSceneLayoutCoordinateSpace initWithParentCoordinateSpace:];
```
