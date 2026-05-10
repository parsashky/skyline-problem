# Skyline Problem

This project provides a Python implementation of the classic **Skyline Problem**, a well-known challenge in computational geometry and algorithm design.

## Problem Description
The skyline problem involves determining the outline of a city skyline formed by multiple rectangular buildings. Each building is represented by three values:

- Left x-coordinate
- Right x-coordinate
- Height

Given a list of buildings, the goal is to compute the **key points** where the skyline changes height when viewed from a distance.

## Approach
The solution processes building start and end events and keeps track of active building heights to determine the visible skyline at each position. Efficient data structures are used to ensure good performance even with large inputs.
