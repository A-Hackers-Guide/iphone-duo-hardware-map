# `SBHardwareButtonActionList`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
q _performQueueNestCount;
B _buttonDown;
@"NSMutableArray" _actionBlocks;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_actionBlocks) actionBlocks;
@property (TB,N,GisButtonDown,V_buttonDown) buttonDown;
```

## Instance methods

```
-[SBHardwareButtonActionList isButtonDown];
-[SBHardwareButtonActionList setButtonDown:];
-[SBHardwareButtonActionList actionBlocks];
-[SBHardwareButtonActionList performQueuedButtonUpActions];
-[SBHardwareButtonActionList scheduleButtonUpActionBlock:];
-[SBHardwareButtonActionList setActionBlocks:];
```
