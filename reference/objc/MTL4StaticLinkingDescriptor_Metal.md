# `MTL4StaticLinkingDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _functionDescriptors;
@"NSArray" _privateFunctionDescriptors;
@"NSDictionary" _groups;
```

## Properties

```
@property (T@"NSArray",C,N,V_functionDescriptors) functionDescriptors;
@property (T@"NSArray",C,N,V_privateFunctionDescriptors) privateFunctionDescriptors;
@property (T@"NSDictionary",C,N,V_groups) groups;
```

## Instance methods

```
-[MTL4StaticLinkingDescriptor init];
-[MTL4StaticLinkingDescriptor dealloc];
-[MTL4StaticLinkingDescriptor setGroups:];
-[MTL4StaticLinkingDescriptor groups];
-[MTL4StaticLinkingDescriptor hash];
-[MTL4StaticLinkingDescriptor copyWithZone:];
-[MTL4StaticLinkingDescriptor isEqual:];
-[MTL4StaticLinkingDescriptor functionDescriptors];
-[MTL4StaticLinkingDescriptor privateFunctionDescriptors];
-[MTL4StaticLinkingDescriptor setFunctionDescriptors:];
-[MTL4StaticLinkingDescriptor setPrivateFunctionDescriptors:];
```
