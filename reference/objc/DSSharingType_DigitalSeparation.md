# `DSSharingType`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"<DSSource>" _source;
@"NSMutableOrderedSet" _people;
```

## Properties

```
@property (T@"<DSSource>",&,N,V_source) source;
@property (T@"NSMutableOrderedSet",&,N,V_people) people;
@property (Tq,R,N) score;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) localizedDetailText;
@property (T@"NSArray",R,C,N) sortedPeople;
@property (T@"NSArray",R,C,N) allPeople;
```

## Class methods

```
+[DSSharingType initialize];
```

## Instance methods

```
-[DSSharingType addPerson:];
-[DSSharingType initWithSource:];
-[DSSharingType setPeople:];
-[DSSharingType people];
-[DSSharingType displayName];
-[DSSharingType sortedPeople];
-[DSSharingType score];
-[DSSharingType setSource:];
-[DSSharingType valueForKey:];
-[DSSharingType hash];
-[DSSharingType isEqual:];
-[DSSharingType source];
-[DSSharingType allPeople];
-[DSSharingType removePerson:];
-[DSSharingType localizedDetailText];
-[DSSharingType stopAllSharingOnQueue:completion:];
-[DSSharingType stopSharingPeople:queue:completion:];
-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:];
```
