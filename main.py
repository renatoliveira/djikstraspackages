#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Grafo:
    def __init__(self, packages_file_name, path_file_name, result_file_name):
        self.nodes = set()
        self.adjacents = dict()
        self.distances = {}
        self.result_file_name = result_file_name

        if os.path.exists(packages_file_name) and os.path.exists(path_file_name):
            pkgs_file = open(packages_file_name, 'r')
            paths_file = open(path_file_name, 'r')

            for path in paths_file:
                split = path.replace('\n', '').split(' ')
                if len(split) == 3:
                    self.add_node(split[0])
                    self.add_node(split[1])
                    self.add_path(split[0], split[1], int(split[2]))

            for pkg in pkgs_file:
                split = pkg.replace('\n', '').split(' ')
                if len(split) == 2:
                    self.get_path(split[0], split[1])

            pkgs_file.close()
            paths_file.close()

    def add_node(self, node):
        self.nodes.add(node)

    def add_path(self, ori, des, dis):
        if ori in self.adjacents:
            self.adjacents[ori].append(des)
        else:
            self.adjacents[ori] = []
            self.adjacents[ori].append(des)

        if des in self.adjacents:
            self.adjacents[des].append(ori)
        else:
            self.adjacents[des] = []
            self.adjacents[des].append(ori)

        self.adjacents[des] = sorted(list(set(self.adjacents[des])))
        self.adjacents[ori] = sorted(list(set(self.adjacents[ori])))
        
        self.distances[(ori, des)] = dis

    def get_path(self, origin, destination):
        while True:
            for connection in nodes:
                if connection in visited:
                    if closest_node is None:
                        closest_node = connection
                    elif visited[connection] < visited[closest_node]:
                        closest_node = connection

            if closest_node is None:
                break

            nodes.remove(closest_node)

            current_weight = visited[closest_node]
            for node in self.adjacents[closest_node]:
                weight = current_weight + self.distances[(closest_node, node)]
                if node not in visited or weight < visited[node]:
                    visited[node] = weight
                    path[node] = closest_node

        self.write_result(visited, path, origin, destination)

    def write_result(self, amounts, closest, origin, destination):
        f = open(self.result_file_name, 'a')
        f.write(self.format_route(closest, destination) + ' ' + destination + ' ' + str(amounts[destination]) + '\n')
        f.close()

    def format_route(self, route, current):
        path = []
        while True:
            if current in route:
                path.append(route[current])
                current = route[current]
            else:
                break
        path.reverse()
        return ' '.join(path)

grafo = Grafo('packages.txt', 'paths.txt', 'routes.txt')
