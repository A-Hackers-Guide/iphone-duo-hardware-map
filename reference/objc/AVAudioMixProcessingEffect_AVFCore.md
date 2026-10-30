# `AVAudioMixProcessingEffect`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioMixEffect`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _graphText;
@"NSMutableArray" _scheduleEntries;
@"NSDictionary" _properties;
```

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) DSPGraphText;
@property (T@"NSDictionary",R,N) properties;
@property (T@"NSArray",R,N) parameterSchedule;
```

## Class methods

```
+[AVAudioMixProcessingEffect processingEffectWithDSPGraphText:properties:parameterSchedule:identifier:];
```

## Instance methods

```
-[AVAudioMixProcessingEffect properties];
-[AVAudioMixProcessingEffect identifier];
-[AVAudioMixProcessingEffect dealloc];
-[AVAudioMixProcessingEffect hash];
-[AVAudioMixProcessingEffect description];
-[AVAudioMixProcessingEffect copyWithZone:];
-[AVAudioMixProcessingEffect isEqual:];
-[AVAudioMixProcessingEffect DSPGraphText];
-[AVAudioMixProcessingEffect _figAudioProperties];
-[AVAudioMixProcessingEffect _figIdentifier];
-[AVAudioMixProcessingEffect _figSchedule];
-[AVAudioMixProcessingEffect _fourCCToFigPropertyDict];
-[AVAudioMixProcessingEffect initWithDSPGraphText:properties:parameterSchedule:identifier:];
-[AVAudioMixProcessingEffect isValueSupported:exceptionReasonOut:];
-[AVAudioMixProcessingEffect parameterSchedule];
```
