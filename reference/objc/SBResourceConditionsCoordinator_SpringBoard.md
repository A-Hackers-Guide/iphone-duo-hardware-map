# `SBResourceConditionsCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSHashTable" _foregroundScenes;
@"NSHashTable" _assistantIslandActiveScenes;
Q _memoryPressure;
```

## Properties

```
@property (TQ,R,N,V_memoryPressure) memoryPressure;
```

## Instance methods

```
-[SBResourceConditionsCoordinator removeObserver:];
-[SBResourceConditionsCoordinator init];
-[SBResourceConditionsCoordinator addObserver:];
-[SBResourceConditionsCoordinator memoryPressure];
-[SBResourceConditionsCoordinator _recomputeMemoryPressure];
-[SBResourceConditionsCoordinator scene:didChangeAssistantIslandActiveStateTo:];
-[SBResourceConditionsCoordinator scene:didChangeForegroundStateTo:];
-[SBResourceConditionsCoordinator scene:didChangeParentSceneTo:];
```
