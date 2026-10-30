# `CMSWOLFSummary`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 9 instance variables, 9 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSDate" fStartDate;
@"NSDate" fEndDate;
@"NSUUID" fSourceId;
@"NSUUID" fSessionId;
d fSWOLF;
d fFreestyleSWOLF;
d fBackstrokeSWOLF;
d fBreaststrokeSWOLF;
d fButterflySWOLF;
```

## Properties

```
@property (T@"NSData",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (T@"NSUUID",R,N) sessionId;
@property (T@"NSUUID",R,N) sourceId;
@property (Td,R,N) SWOLF;
@property (Td,R,N) freestyleSWOLF;
@property (Td,R,N) backstrokeSWOLF;
@property (Td,R,N) breaststrokeSWOLF;
@property (Td,R,N) butterflySWOLF;
```

## Class methods

```
+[CMSWOLFSummary supportsSecureCoding];
```

## Instance methods

```
-[CMSWOLFSummary startDate];
-[CMSWOLFSummary sourceId];
-[CMSWOLFSummary sessionId];
-[CMSWOLFSummary dealloc];
-[CMSWOLFSummary endDate];
-[CMSWOLFSummary encodeWithCoder:];
-[CMSWOLFSummary description];
-[CMSWOLFSummary initWithCoder:];
-[CMSWOLFSummary copyWithZone:];
-[CMSWOLFSummary SWOLF];
-[CMSWOLFSummary backstrokeSWOLF];
-[CMSWOLFSummary breaststrokeSWOLF];
-[CMSWOLFSummary butterflySWOLF];
-[CMSWOLFSummary freestyleSWOLF];
-[CMSWOLFSummary initWithCLSWOLFSummary:];
-[CMSWOLFSummary initWithSessionId:sourceId:startDate:endDate:SWOLF:freestyleSWOLF:backstrokeSWOLF:breaststrokeSWOLF:butterflySWOLF:];
```
