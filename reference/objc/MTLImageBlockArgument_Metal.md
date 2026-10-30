# `MTLImageBlockArgument`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- 5 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _kind;
I _dataSize;
@"MTLStructTypeInternal" _masterStructMembers;
B _aliasImplicitImageBlock;
I _aliasImplicitImageBlockRenderTarget;
```

## Instance methods

```
-[MTLImageBlockArgument dealloc];
-[MTLImageBlockArgument setStructType:];
-[MTLImageBlockArgument isEqual:];
-[MTLImageBlockArgument aliasImplicitImageBlock];
-[MTLImageBlockArgument aliasImplicitImageBlockRenderTarget];
-[MTLImageBlockArgument imageBlockDataSize];
-[MTLImageBlockArgument imageBlockKind];
-[MTLImageBlockArgument imageBlockMasterStructMembers];
-[MTLImageBlockArgument initWithName:type:access:isActive:index:kind:dataSize:masterStructMembers:aliasImplicitImageBlock:aliasImplicitImageBlockRenderTarget:];
```
