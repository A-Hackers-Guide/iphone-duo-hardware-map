# `BWStillImageDuplicateInfo`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _originalPresentationTimestamp;
{?="value"q"timescale"i"flags"I"epoch"q} _sbufPresentationTimestamp;
q _settingsID;
```

## Properties

```
@property (T{?=qiIq},N,V_originalPresentationTimestamp) originalPresentationTimestamp;
@property (T{?=qiIq},N,V_sbufPresentationTimestamp) sbufPresentationTimestamp;
@property (Tq,N,V_settingsID) settingsID;
```

## Class methods

```
+[BWStillImageDuplicateInfo supportsSecureCoding];
```

## Instance methods

```
-[BWStillImageDuplicateInfo initWithDictionaryRepresentation:];
-[BWStillImageDuplicateInfo init];
-[BWStillImageDuplicateInfo settingsID];
-[BWStillImageDuplicateInfo encodeWithCoder:];
-[BWStillImageDuplicateInfo setSettingsID:];
-[BWStillImageDuplicateInfo hash];
-[BWStillImageDuplicateInfo description];
-[BWStillImageDuplicateInfo initWithCoder:];
-[BWStillImageDuplicateInfo isEqual:];
-[BWStillImageDuplicateInfo dictionaryRepresentation];
-[BWStillImageDuplicateInfo originalPresentationTimestamp];
-[BWStillImageDuplicateInfo sbufPresentationTimestamp];
-[BWStillImageDuplicateInfo setOriginalPresentationTimestamp:];
-[BWStillImageDuplicateInfo setSbufPresentationTimestamp:];
```
