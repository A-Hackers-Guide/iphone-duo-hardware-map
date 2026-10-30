# `AVParameterEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
{ParameterEvent="parameterID"I"scope"I"element"I"value"f} _event;
```

## Properties

```
@property (T^{ParameterEvent=IIIf},R) event;
@property (TI) parameterID;
@property (TI) scope;
@property (TI) element;
@property (Tf) value;
```

## Instance methods

```
-[AVParameterEvent setElement:];
-[AVParameterEvent element];
-[AVParameterEvent scope];
-[AVParameterEvent value];
-[AVParameterEvent event];
-[AVParameterEvent setValue:];
-[AVParameterEvent setScope:];
-[AVParameterEvent parameterID];
-[AVParameterEvent setParameterID:];
-[AVParameterEvent initWithParameterEvent:];
-[AVParameterEvent initWithParameterID:scope:element:value:];
```
