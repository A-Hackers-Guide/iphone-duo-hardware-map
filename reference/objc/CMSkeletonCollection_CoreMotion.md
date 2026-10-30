# `CMSkeletonCollection`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _localMachtime;
d _globalMachtime;
@"NSArray" _skeleton2D;
@"NSArray" _skeleton3DLifted;
@"NSArray" _skeleton3DRetargeted;
```

## Properties

```
@property (Td,N,V_localMachtime) localMachtime;
@property (Td,N,V_globalMachtime) globalMachtime;
@property (T@"NSArray",&,N,V_skeleton2D) skeleton2D;
@property (T@"NSArray",&,N,V_skeleton3DLifted) skeleton3DLifted;
@property (T@"NSArray",&,N,V_skeleton3DRetargeted) skeleton3DRetargeted;
```

## Instance methods

```
-[CMSkeletonCollection globalMachtime];
-[CMSkeletonCollection localMachtime];
-[CMSkeletonCollection setGlobalMachtime:];
-[CMSkeletonCollection setLocalMachtime:];
-[CMSkeletonCollection setSkeleton2D:];
-[CMSkeletonCollection setSkeleton3DLifted:];
-[CMSkeletonCollection setSkeleton3DRetargeted:];
-[CMSkeletonCollection skeleton2D];
-[CMSkeletonCollection skeleton3DLifted];
-[CMSkeletonCollection skeleton3DRetargeted];
```
