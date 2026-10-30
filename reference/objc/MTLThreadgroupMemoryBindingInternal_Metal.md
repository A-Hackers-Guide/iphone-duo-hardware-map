# `MTLThreadgroupMemoryBindingInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- Protocols: `MTLThreadgroupBinding`
- 3 instance variables, 12 properties, 10 instance methods, 0 class methods

## Instance variables

```
S _alignment;
I _dataSize;
Q _dataType;
```

## Properties

```
@property (TQ,R) threadgroupMemoryAlignment;
@property (TQ,R) threadgroupMemoryDataSize;
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
-[MTLThreadgroupMemoryBindingInternal formattedDescription:];
-[MTLThreadgroupMemoryBindingInternal setStructType:doRetain:];
-[MTLThreadgroupMemoryBindingInternal setStructType:];
-[MTLThreadgroupMemoryBindingInternal structType];
-[MTLThreadgroupMemoryBindingInternal isEqual:];
-[MTLThreadgroupMemoryBindingInternal initWithName:type:access:isActive:locationIndex:arraySize:dataType:dataSize:alignment:];
-[MTLThreadgroupMemoryBindingInternal threadgroupMemoryAlignment];
-[MTLThreadgroupMemoryBindingInternal threadgroupMemoryDataSize];
-[MTLThreadgroupMemoryBindingInternal threadgroupMemoryDataType];
-[MTLThreadgroupMemoryBindingInternal threadgroupMemoryStructType];
```
