# `PKInkFeatheringDescriptor`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 1 class methods

## Instance variables

```
d _startCapTime;
d _startCapDistance;
d _startCapFade;
d _startCapShrink;
d _endCapTime;
d _endCapDistance;
d _endCapFade;
d _endCapShrink;
```

## Properties

```
@property (Td,N,V_startCapTime) startCapTime;
@property (Td,N,V_startCapDistance) startCapDistance;
@property (Td,N,V_startCapFade) startCapFade;
@property (Td,N,V_startCapShrink) startCapShrink;
@property (Td,N,V_endCapTime) endCapTime;
@property (Td,N,V_endCapDistance) endCapDistance;
@property (Td,N,V_endCapFade) endCapFade;
@property (Td,N,V_endCapShrink) endCapShrink;
```

## Class methods

```
+[PKInkFeatheringDescriptor descriptorWithStartCapTime:startCapFade:endCapTime:endCapFade:];
```

## Instance methods

```
-[PKInkFeatheringDescriptor mutableCopy];
-[PKInkFeatheringDescriptor endCapDistance];
-[PKInkFeatheringDescriptor endCapFade];
-[PKInkFeatheringDescriptor endCapShrink];
-[PKInkFeatheringDescriptor endCapTime];
-[PKInkFeatheringDescriptor initWithStartCapTime:startCapDistance:startCapFade:startCapShrink:endCapTime:endCapDistance:endCapFade:endCapShrink:];
-[PKInkFeatheringDescriptor setEndCapDistance:];
-[PKInkFeatheringDescriptor setEndCapFade:];
-[PKInkFeatheringDescriptor setEndCapShrink:];
-[PKInkFeatheringDescriptor setEndCapTime:];
-[PKInkFeatheringDescriptor setStartCapDistance:];
-[PKInkFeatheringDescriptor setStartCapFade:];
-[PKInkFeatheringDescriptor setStartCapShrink:];
-[PKInkFeatheringDescriptor setStartCapTime:];
-[PKInkFeatheringDescriptor startCapDistance];
-[PKInkFeatheringDescriptor startCapFade];
-[PKInkFeatheringDescriptor startCapShrink];
-[PKInkFeatheringDescriptor startCapTime];
```
