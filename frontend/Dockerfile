# Serve prebuilt frontend with Nginx
FROM nginx:alpine

# Copy the prebuilt frontend from your local machine
COPY dist /usr/share/nginx/html

# Expose HTTP port
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
