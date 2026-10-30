# `MTLStructTypeInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLStructType`
- 5 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
Q _dataType;
@"NSDictionary" _dictionary;
@"NSArray" _members;
B _isIndirectArgumentBuffer;
@"NSString" _typeName;
```

## Properties

```
@property (TB,V_isIndirectArgumentBuffer) isIndirectArgumentBuffer;
@property (T@"NSString",R,V_typeName) typeName;
```

## Instance methods

```
-[MTLStructTypeInternal initWithMembers:count:typeName:];
-[MTLStructTypeInternal typeName];
-[MTLStructTypeInternal memberByName:];
-[MTLStructTypeInternal setIsIndirectArgumentBuffer:];
-[MTLStructTypeInternal init];
-[MTLStructTypeInternal dealloc];
-[MTLStructTypeInternal isIndirectArgumentBuffer];
-[MTLStructTypeInternal initWithMembers:count:];
-[MTLStructTypeInternal formattedDescription:withPrintedTypes:];
-[MTLStructTypeInternal dataType];
-[MTLStructTypeInternal description];
-[MTLStructTypeInternal setMembers:count:];
-[MTLStructTypeInternal members];
-[MTLStructTypeInternal isEqual:];
-[MTLStructTypeInternal isStructLayoutThreadSafeWith:];
```
