# `SRSpeechExpression`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSString" _version;
d _confidence;
d _mood;
d _valence;
d _activation;
d _dominance;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
```

## Properties

```
@property (T@"NSString",R,C,N,V_version) version;
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_timeRange) timeRange;
@property (Td,R,N,V_confidence) confidence;
@property (Td,R,N,V_mood) mood;
@property (Td,R,N,V_valence) valence;
@property (Td,R,N,V_activation) activation;
@property (Td,R,N,V_dominance) dominance;
```

## Class methods

```
+[SRSpeechExpression supportsSecureCoding];
+[SRSpeechExpression new];
```

## Instance methods

```
-[SRSpeechExpression timeRange];
-[SRSpeechExpression init];
-[SRSpeechExpression dealloc];
-[SRSpeechExpression version];
-[SRSpeechExpression encodeWithCoder:];
-[SRSpeechExpression hash];
-[SRSpeechExpression description];
-[SRSpeechExpression initWithCoder:];
-[SRSpeechExpression copyWithZone:];
-[SRSpeechExpression isEqual:];
-[SRSpeechExpression confidence];
-[SRSpeechExpression mood];
-[SRSpeechExpression valence];
-[SRSpeechExpression activation];
-[SRSpeechExpression dominance];
-[SRSpeechExpression initWithVersion:timeRange:confidence:mood:valence:activation:dominance:];
```
