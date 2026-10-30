# `ASEProcessing`

- Image: [`/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`](../userland/System__Library__PrivateFrameworks__ASEProcessing.framework__ASEProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"ASEProcessingT0" _ase;
B _inputType;
f _enhancementStrength;
I _destinationWidth;
I _destinationHeight;
```

## Properties

```
@property (Tf,N,V_enhancementStrength) enhancementStrength;
@property (TI,N,V_destinationWidth) destinationWidth;
@property (TI,N,V_destinationHeight) destinationHeight;
@property (TB,N,V_inputType) inputType;
```

## Class methods

```
+[ASEProcessing shouldEnhanceWidth:height:destinationWidth:destinationHeight:];
+[ASEProcessing shouldEnhanceWidth:height:destinationWidth:destinationHeight:fps:];
```

## Instance methods

```
-[ASEProcessing initWithConfig:];
-[ASEProcessing init];
-[ASEProcessing inputType];
-[ASEProcessing setInputType:];
-[ASEProcessing processFrameWithInput:Measurement:outputData:];
-[ASEProcessing processFrameWithInput:outputData:];
-[ASEProcessing setDestinationHeight:];
-[ASEProcessing setDestinationWidth:];
-[ASEProcessing enhancementStrength];
-[ASEProcessing setEnhancementStrength:];
-[ASEProcessing processFrameWithInput:callback:];
-[ASEProcessing destinationHeight];
-[ASEProcessing destinationWidth];
-[ASEProcessing getDestinationHeight];
-[ASEProcessing getDestinationWidth];
-[ASEProcessing getEnhancementStrength];
-[ASEProcessing processFrameWithInput:Measurement:Output:];
-[ASEProcessing processFrameWithInput:Measurement:callback:];
-[ASEProcessing processFrameWithInput:Output:];
```
