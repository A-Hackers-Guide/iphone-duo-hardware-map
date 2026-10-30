# `BWTimeSkew`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _native;
{?="value"q"timescale"i"flags"I"epoch"q} _original;
{?="value"q"timescale"i"flags"I"epoch"q} _adjusted;
B _isBracketFrame;
B _isSISFrame;
B _isStartOfDiscontinuity;
```

## Properties

```
@property (T{?=qiIq},R,N,V_native) native;
@property (T{?=qiIq},R,N,V_original) original;
@property (T{?=qiIq},N,V_adjusted) adjusted;
@property (TB,R,N,V_isBracketFrame) isBracketFrame;
@property (TB,R,N,V_isSISFrame) isSISFrame;
@property (TB,N,V_isStartOfDiscontinuity) isStartOfDiscontinuity;
```

## Instance methods

```
-[BWTimeSkew native];
-[BWTimeSkew description];
-[BWTimeSkew copyWithZone:];
-[BWTimeSkew original];
-[BWTimeSkew adjusted];
-[BWTimeSkew initWithNativeTime:originalTime:isBracketFrame:isSISFrame:];
-[BWTimeSkew isBracketFrame];
-[BWTimeSkew isSISFrame];
-[BWTimeSkew isStartOfDiscontinuity];
-[BWTimeSkew setAdjusted:];
-[BWTimeSkew setIsStartOfDiscontinuity:];
```
