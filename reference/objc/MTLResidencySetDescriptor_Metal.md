# `MTLResidencySetDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _label;
Q _initialCapacity;
B _evictsImmediately;
```

## Properties

```
@property (T@"NSString",C,N,V_label) label;
@property (TQ,N,V_initialCapacity) initialCapacity;
```

## Instance methods

```
-[MTLResidencySetDescriptor init];
-[MTLResidencySetDescriptor label];
-[MTLResidencySetDescriptor setLabel:];
-[MTLResidencySetDescriptor dealloc];
-[MTLResidencySetDescriptor initialCapacity];
-[MTLResidencySetDescriptor commitsImmediately];
-[MTLResidencySetDescriptor setCommitsImmediately:];
-[MTLResidencySetDescriptor hash];
-[MTLResidencySetDescriptor setInitialCapacity:];
-[MTLResidencySetDescriptor copyWithZone:];
-[MTLResidencySetDescriptor isEqual:];
-[MTLResidencySetDescriptor evictsImmediately];
-[MTLResidencySetDescriptor setEvictsImmediately:];
```
