var force = d3.layout.force()
      .charge(-350)
      .linkDistance(300)
      .nodes(graph.nodes)
      .links(graph.links)
      .size([800, 800]);

  var svg = d3.select('body').html('')
      .append('svg')
      .attr('width', 800)
      .attr('height', 800);

  var node = svg.selectAll(".node");
  var edge = svg.selectAll('line.edge');

  force.on('tick', function() {
          for(var i=0; i<graph.nodes.length; i++) {
              if (graph.nodes[i].name == 'lovewins') {
                  graph.nodes[i].x = 400;
                  graph.nodes[i].y = 400;
                  break;
              }
          }

          node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

          edge.attr('x1', function(d) { return d.source.x; })
              .attr('y1', function(d) { return d.source.y; })
              .attr('x2', function(d) { return d.target.x; })
              .attr('y2', function(d) { return d.target.y; });
  });

  function draw_graph() {
      // Add the edges to the SVG.
      edge = edge.data(graph.links);
      edge.enter().append('line')
          .attr('class', 'edge')
          .style('stroke', 'rgba(200, 100, 200, 0.2)')
          .style('stroke-width', 2.0);
      edge.exit();

      // Add the nodes to the SVG.
      node = node.data(graph.nodes);
      var insidenode = node.enter().append("g");
      insidenode.attr("class", "node")
          .call(force.drag);

      insidenode.append("circle")
          .attr("r", 8);

      insidenode.append("text")
          .attr("x", 12)
          .attr("dy", ".35em")
          .text(function(d) { return d.name; });

      node.exit();

      // Start the visualization.
      force.nodes(graph.nodes).links(graph.links).start();
  }

  var eventSrc  = new EventSource('/data');
  eventSrc.addEventListener('message', function (event) {
      var graphData = JSON.parse(event.data);
      graphData.nodes.forEach(function(v) { graph.nodes.push(v) });
      graphData.links.forEach(function(v) { graph.links.push(v) });

      draw_graph();
  });
