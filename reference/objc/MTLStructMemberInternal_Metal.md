# `MTLStructMemberInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLStructMember`
- 10 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
Q _offset;
b16 _dataType;
@ _details;
Q _pixelFormat;
Q _aluType;
Q _argumentIndex;
Q _render_target;
Q _raster_order_group;
@"MTLType" _typeInfo;
```

## Properties

```
@property (TQ,R,V_pixelFormat) pixelFormat;
@property (TQ,R,V_aluType) aluType;
@property (TQ,R,V_render_target) render_target;
@property (TQ,R,V_raster_order_group) raster_order_group;
```

## Instance methods

```
-[MTLStructMemberInternal raster_order_group];
-[MTLStructMemberInternal dealloc];
-[MTLStructMemberInternal aluType];
-[MTLStructMemberInternal isMemberLayoutThreadSafeWith:];
-[MTLStructMemberInternal pointerType];
-[MTLStructMemberInternal tensorReferenceType];
-[MTLStructMemberInternal structType];
-[MTLStructMemberInternal indirectArgumentType];
-[MTLStructMemberInternal render_target];
-[MTLStructMemberInternal initWithName:offset:dataType:pixelFormat:aluType:indirectArgumentIndex:render_target:raster_order_group:details:];
-[MTLStructMemberInternal formattedDescription:withPrintedTypes:];
-[MTLStructMemberInternal dataType];
-[MTLStructMemberInternal indirectArgumentIndex];
-[MTLStructMemberInternal pixelFormat];
-[MTLStructMemberInternal setOffset:];
-[MTLStructMemberInternal textureReferenceType];
-[MTLStructMemberInternal argumentIndex];
-[MTLStructMemberInternal isEqual:];
-[MTLStructMemberInternal dataTypeDescription];
-[MTLStructMemberInternal name];
-[MTLStructMemberInternal offset];
-[MTLStructMemberInternal arrayType];
```
