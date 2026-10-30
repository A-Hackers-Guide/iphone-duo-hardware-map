# `CLFindMyAccessoryFragmentAccumulator`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _uuidToData;
Q _maxBytesPerUUID;
```

## Properties

```
@property (T@"NSMutableDictionary",N,V_uuidToData) uuidToData;
@property (TQ,N,V_maxBytesPerUUID) maxBytesPerUUID;
```

## Class methods

```
+[CLFindMyAccessoryFragmentAccumulator convertDataStatusToString:];
```

## Instance methods

```
-[CLFindMyAccessoryFragmentAccumulator dealloc];
-[CLFindMyAccessoryFragmentAccumulator maxBytesPerUUID];
-[CLFindMyAccessoryFragmentAccumulator appendData:forUUID:];
-[CLFindMyAccessoryFragmentAccumulator clearForUUID:];
-[CLFindMyAccessoryFragmentAccumulator dataForUUID:];
-[CLFindMyAccessoryFragmentAccumulator getDataStatusForUUID:];
-[CLFindMyAccessoryFragmentAccumulator initWithMaxBytesPerUUID:];
-[CLFindMyAccessoryFragmentAccumulator setMaxBytesPerUUID:];
-[CLFindMyAccessoryFragmentAccumulator setUuidToData:];
-[CLFindMyAccessoryFragmentAccumulator uuidToData];
```
