# `DSBlockingFetchResult`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
? sharingPeople;
@"NSError" fetchError;
? emergencyContacts;
B removedEmergencyContacts;
```

## Properties

```
@property (T@"NSArray",N,R) sharingPeople;
@property (T@"NSError",N,R,VfetchError) fetchError;
@property (T@"NSArray",N,R) emergencyContacts;
@property (TB,N,R) isSharing;
@property (TB,N,R) isSharingLocation;
@property (T@"NSArray",N,R) displayNames;
@property (T@"NSArray",N,R) displayGivenNames;
@property (TB,N,VremovedEmergencyContacts) removedEmergencyContacts;
```

## Instance methods

```
-[DSBlockingFetchResult init];
-[DSBlockingFetchResult fetchError];
-[DSBlockingFetchResult displayNames];
-[DSBlockingFetchResult emergencyContacts];
-[DSBlockingFetchResult displayGivenNames];
-[DSBlockingFetchResult initWithPeople:emergencyContacts:error:];
-[DSBlockingFetchResult isSharing];
-[DSBlockingFetchResult isSharingLocation];
-[DSBlockingFetchResult removedEmergencyContacts];
-[DSBlockingFetchResult setRemovedEmergencyContacts:];
-[DSBlockingFetchResult sharingPeople];
```
