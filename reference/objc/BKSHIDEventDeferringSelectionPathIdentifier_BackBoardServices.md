# `BKSHIDEventDeferringSelectionPathIdentifier`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`, `BSProtobufSerializable`, `NSCopying`, `BKSHIDEventDeferringSelectionPathSymbol`
- 1 instance variables, 5 properties, 11 instance methods, 5 class methods

## Instance variables

```
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringSelectionPathIdentifier supportsSecureCoding];
+[BKSHIDEventDeferringSelectionPathIdentifier protobufSchema];
+[BKSHIDEventDeferringSelectionPathIdentifier everySelectionPath];
+[BKSHIDEventDeferringSelectionPathIdentifier primary];
+[BKSHIDEventDeferringSelectionPathIdentifier genericGesture];
```

## Instance methods

```
-[BKSHIDEventDeferringSelectionPathIdentifier didFinishProtobufDecodingWithError:];
-[BKSHIDEventDeferringSelectionPathIdentifier identifier];
-[BKSHIDEventDeferringSelectionPathIdentifier _substituteSingeltonForIdentifierString:];
-[BKSHIDEventDeferringSelectionPathIdentifier encodeWithCoder:];
-[BKSHIDEventDeferringSelectionPathIdentifier hash];
-[BKSHIDEventDeferringSelectionPathIdentifier description];
-[BKSHIDEventDeferringSelectionPathIdentifier initWithCoder:];
-[BKSHIDEventDeferringSelectionPathIdentifier appendDescriptionToStream:];
-[BKSHIDEventDeferringSelectionPathIdentifier copyWithZone:];
-[BKSHIDEventDeferringSelectionPathIdentifier isEqual:];
-[BKSHIDEventDeferringSelectionPathIdentifier initWithIdentifier:];
```
