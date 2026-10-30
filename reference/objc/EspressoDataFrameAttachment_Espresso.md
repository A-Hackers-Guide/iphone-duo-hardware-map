# `EspressoDataFrameAttachment`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _disabled;
@"NSString" _filePath;
^v _rawPointer;
Q _offset;
Q _size;
```

## Properties

```
@property (T@"NSString",&,V_filePath) filePath;
@property (T^v,V_rawPointer) rawPointer;
@property (TQ,V_offset) offset;
@property (TQ,V_size) size;
@property (TB,V_disabled) disabled;
```

## Class methods

```
+[EspressoDataFrameAttachment fromDict:frameStorage:];
```

## Instance methods

```
-[EspressoDataFrameAttachment disabled];
-[EspressoDataFrameAttachment size];
-[EspressoDataFrameAttachment filePath];
-[EspressoDataFrameAttachment setOffset:];
-[EspressoDataFrameAttachment setFilePath:];
-[EspressoDataFrameAttachment setDisabled:];
-[EspressoDataFrameAttachment offset];
-[EspressoDataFrameAttachment setSize:];
-[EspressoDataFrameAttachment loadFromDict:frameStorage:];
-[EspressoDataFrameAttachment rawPointer];
-[EspressoDataFrameAttachment setRawPointer:];
```
