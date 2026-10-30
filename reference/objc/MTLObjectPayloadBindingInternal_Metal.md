# `MTLObjectPayloadBindingInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- Protocols: `MTLObjectPayloadBinding`
- 3 instance variables, 12 properties, 11 instance methods, 0 class methods

## Instance variables

```
S _alignment;
I _dataSize;
Q _dataType;
```

## Properties

```
@property (TQ,R) objectPayloadAlignment;
@property (TQ,R) objectPayloadDataSize;
@property (T@"NSString",R) name;
@property (Tq,R) type;
@property (TQ,R) access;
@property (TQ,R) index;
@property (TB,R,GisUsed) used;
@property (TB,R,GisArgument) argument;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLObjectPayloadBindingInternal formattedDescription:];
-[MTLObjectPayloadBindingInternal setStructType:doRetain:];
-[MTLObjectPayloadBindingInternal setStructType:];
-[MTLObjectPayloadBindingInternal structType];
-[MTLObjectPayloadBindingInternal isEqual:];
-[MTLObjectPayloadBindingInternal initWithName:type:access:isActive:arraySize:dataType:dataSize:alignment:];
-[MTLObjectPayloadBindingInternal initWithName:type:access:isActive:locationIndex:arraySize:dataType:dataSize:alignment:];
-[MTLObjectPayloadBindingInternal objectPayloadAlignment];
-[MTLObjectPayloadBindingInternal objectPayloadDataSize];
-[MTLObjectPayloadBindingInternal objectPayloadDataType];
-[MTLObjectPayloadBindingInternal objectPayloadStructType];
```
