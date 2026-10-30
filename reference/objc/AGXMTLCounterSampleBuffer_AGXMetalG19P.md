# `AGXMTLCounterSampleBuffer`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLCounterSampleBuffer`
- 4 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice" _device;
@"NSString" _label;
Q _sampleCount;
@"AGXBuffer" _buffer;
```

## Properties

```
@property (T@"IOGPUMetalBuffer",R) buffer;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (TQ,R) sampleCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXMTLCounterSampleBuffer buffer];
-[AGXMTLCounterSampleBuffer device];
-[AGXMTLCounterSampleBuffer label];
-[AGXMTLCounterSampleBuffer dealloc];
-[AGXMTLCounterSampleBuffer sampleCount];
-[AGXMTLCounterSampleBuffer initWithDevice:descriptor:error:];
-[AGXMTLCounterSampleBuffer sampleSize];
-[AGXMTLCounterSampleBuffer resolveCounterRange:];
-[AGXMTLCounterSampleBuffer initWithDevice:length:label:options:error:];
```
