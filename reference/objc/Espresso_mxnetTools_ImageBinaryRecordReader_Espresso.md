# `Espresso_mxnetTools_ImageBinaryRecordReader`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSFileHandle" _recFileHandle;
{_mxnetTools_recordHeader_t_="magic"I"lrecord"I} _recordHeader;
Q _currentOffset;
@"NSMutableArray" _labelsPrivate;
{_mxnetTools_imageHeader_t_="flag"I"label"f"imageID"{_mxnetTools_imageID_t_="ID"[2Q]}} _imageHeader;
```

## Properties

```
@property (T@"NSFileHandle",&,V_recFileHandle) recFileHandle;
@property (T{_mxnetTools_recordHeader_t_=II},V_recordHeader) recordHeader;
@property (T{_mxnetTools_imageHeader_t_=If{_mxnetTools_imageID_t_=[2Q]}},V_imageHeader) imageHeader;
@property (TQ,V_currentOffset) currentOffset;
@property (T@"NSMutableArray",&,V_labelsPrivate) labelsPrivate;
```

## Instance methods

```
-[Espresso_mxnetTools_ImageBinaryRecordReader labels];
-[Espresso_mxnetTools_ImageBinaryRecordReader imageData];
-[Espresso_mxnetTools_ImageBinaryRecordReader currentOffset];
-[Espresso_mxnetTools_ImageBinaryRecordReader setCurrentOffset:];
-[Espresso_mxnetTools_ImageBinaryRecordReader imageID];
-[Espresso_mxnetTools_ImageBinaryRecordReader setImageHeader:];
-[Espresso_mxnetTools_ImageBinaryRecordReader imageHeader];
-[Espresso_mxnetTools_ImageBinaryRecordReader initWithRecFile:error:];
-[Espresso_mxnetTools_ImageBinaryRecordReader labelsPrivate];
-[Espresso_mxnetTools_ImageBinaryRecordReader nextRecordAndError:];
-[Espresso_mxnetTools_ImageBinaryRecordReader recFileHandle];
-[Espresso_mxnetTools_ImageBinaryRecordReader recordHeader];
-[Espresso_mxnetTools_ImageBinaryRecordReader seekRecordWithID:error:];
-[Espresso_mxnetTools_ImageBinaryRecordReader setLabelsPrivate:];
-[Espresso_mxnetTools_ImageBinaryRecordReader setRecFileHandle:];
-[Espresso_mxnetTools_ImageBinaryRecordReader setRecordHeader:];
```
