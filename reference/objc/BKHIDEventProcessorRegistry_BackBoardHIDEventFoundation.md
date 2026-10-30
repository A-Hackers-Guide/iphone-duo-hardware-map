# `BKHIDEventProcessorRegistry`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventProcessorRegistering`
- 1 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _eventProcessorsByClassName;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDEventProcessorRegistry sharedInstance];
```

## Instance methods

```
-[BKHIDEventProcessorRegistry init];
-[BKHIDEventProcessorRegistry addEventProcessor:];
-[BKHIDEventProcessorRegistry eventProcessorOfClass:];
```
