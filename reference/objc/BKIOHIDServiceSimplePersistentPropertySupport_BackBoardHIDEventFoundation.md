# `BKIOHIDServiceSimplePersistentPropertySupport`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKIOHIDServiceMatchObserver`, `BKIOHIDServicePersistentPropertyHandling`, `BSInvalidatable`
- 3 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"BKIOHIDServiceMatcher" _matcher;
@"BKIOHIDServicePersistentPropertyController" _persistentPropertyController;
@"BKSHIDEventSenderDescriptor" _senderDescriptor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKIOHIDServiceSimplePersistentPropertySupport invalidate];
-[BKIOHIDServiceSimplePersistentPropertySupport matcher:servicesDidMatch:];
-[BKIOHIDServiceSimplePersistentPropertySupport setPersistentProperties:forServicesMatchingDescriptor:];
-[BKIOHIDServiceSimplePersistentPropertySupport handlesPersistentPropertiesForSenderDescriptor:];
-[BKIOHIDServiceSimplePersistentPropertySupport initWithSenderDescriptor:matcherDataProvider:persistentPropertyController:];
```
