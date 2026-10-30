# `UIAvoidanceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _blockades;
@"NSMutableSet" _clients;
i _recurseCount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _avoidanceFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_avoidanceFrame) avoidanceFrame;
```

## Instance methods

```
-[UIAvoidanceCoordinator observeValueForKeyPath:ofObject:change:context:];
-[UIAvoidanceCoordinator init];
-[UIAvoidanceCoordinator dealloc];
-[UIAvoidanceCoordinator avoidanceFrame];
-[UIAvoidanceCoordinator setAvoidanceFrame:];
-[UIAvoidanceCoordinator addAvoidanceObject:];
-[UIAvoidanceCoordinator findBlockadesForName:];
-[UIAvoidanceCoordinator findClientsForBlockade:];
-[UIAvoidanceCoordinator findNamesForBlockade:];
-[UIAvoidanceCoordinator releaseAll:withType:];
-[UIAvoidanceCoordinator removeAvoidanceObject:];
-[UIAvoidanceCoordinator setGroupOfBlockades:forBlockadeIdentifier:];
-[UIAvoidanceCoordinator updateClients:];
```
